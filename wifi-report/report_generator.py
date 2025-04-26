#!/usr/bin/env python3
"""
report_generator.py

Usage:
    python report_generator.py <input.pcapng> <output.html>
"""
import sys
import pyshark
import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

def parse_pcap_summary(pcap_path):
    """
    only_summaries=True, keep_packets=False 로 요약 정보만 빠르게 읽어옵니다.
    protocol 과 source IP 별로 카운트합니다.
    """
    cap = pyshark.FileCapture(
        pcap_path,
        only_summaries=True,
        keep_packets=False
    )
    proto_counts = {}
    ip_counts = {}

    for pkt in cap:
        # summary.protocol 에는 "TCP", "UDP", "ICMPv6", "QUIC" 등 문자열이 들어있습니다.
        proto = pkt.protocol
        proto_counts[proto] = proto_counts.get(proto, 0) + 1

        src = pkt.source
        ip_counts[src] = ip_counts.get(src, 0) + 1

    cap.close()

    proto_df = pd.DataFrame.from_dict(proto_counts, orient='index', columns=['count'])
    ip_df    = pd.DataFrame.from_dict(ip_counts,    orient='index', columns=['count'])
    return proto_df.sort_values('count', ascending=False), ip_df.sort_values('count', ascending=False)

def group_small_protocols(proto_df, threshold_pct=1.0):
    """
    전체 대비 threshold_pct% 미만인 프로토콜은 'Other'로 묶어서
    파이 차트에서 잘 보이도록 합니다.
    """
    total = proto_df['count'].sum()
    df = proto_df.copy()
    df['pct'] = df['count'] / total * 100

    major = df[df['pct'] >= threshold_pct].copy()
    other_count = int(df[df['pct'] < threshold_pct]['count'].sum())
    if other_count > 0:
        major.loc['Other'] = [other_count, other_count / total * 100]

    return major.sort_values('count', ascending=False).drop(columns=['pct'])

def render_html(proto_df, ip_df, output_path):
    """
    Jinja2 템플릿을 이용해 최종 HTML을 생성합니다.
    templates/report.html 을 참조하니, 그 위치를 유지하세요.
    """
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    tpl = env.get_template('report.html')
    html = tpl.render(
        protocols=proto_df.reset_index().rename(columns={'index': 'protocol'}),
        top_ips=ip_df.head(10).reset_index().rename(columns={'index': 'ip'})
    )
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Report generated: {output_path}")

def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    pcap_file = sys.argv[1]
    out_html  = sys.argv[2]

    # 1) 요약 정보로 빠르게 집계
    proto_df, ip_df = parse_pcap_summary(pcap_file)
    # 2) 1% 미만인 것은 Other로 묶기
    grouped_proto_df = group_small_protocols(proto_df, threshold_pct=1.0)
    # 3) HTML 생성
    render_html(grouped_proto_df, ip_df, out_html)

if __name__ == '__main__':
    main()

