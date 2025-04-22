**Glassmorphism Star Modal Project**

예쁜 Glassmorphism 카드와 모달 팝업을 구현한 예제입니다. 이 프로젝트는 HTML, CSS, JavaScript를 활용해 다음과 같은 효과를 제공합니다:

- **Glassmorphism 카드**: 반투명 배경, 블러 필터, 부드러운 그림자
- **다양한 테마**: 카드와 모달 각각 4가지 테마 지원
- **모달 팝업**: 카드 클릭 시 모달이 열리고, 배경 반투명 처리
- **별자리 효과**: 모달 내부에서 반짝이는 별이 랜덤 생성되고, 지정된 패턴으로 선 연결
- **애니메이션**: 모달 페이드/슬라이드 인, 별의 트윙클/드리프트

---

## 🔧 설치 및 사용 방법

1. 프로젝트 파일을 로컬에 복사합니다.
2. `index.html` 파일을 브라우저에서 엽니다.

```bash
# 클론 또는 파일 복사
git clone https://github.com/keunoh/Upwork-project.git
cd Upwork-project
open index.html
```

3. 페이지에서 원하는 카드를 클릭하면 모달이 뜹니다.

---

## 🌈 테마 설정

카드와 모달에는 `theme1`~`theme4` 클래스를 통해 4가지 색상 테마를 제공합니다.

```html
<div class="card theme1" onclick="openModal('Title','Text','modal-theme1')">
  ...
</div>
```

---

## ⭐ 별자리 패턴 커스터마이징

`CONSTELLATIONS` 객체를 수정해 각 테마에 맞는 별자리 좌표를 설정할 수 있습니다.

```js
const CONSTELLATIONS = {
  'modal-theme1': [ { x:0.2, y:0.3 }, ... ],
  // ...
};
```

---

## 📋 주요 코드 구조

#### HTML
```html
<div class="grid">
  <div class="card theme1" onclick="openModal('Shine','You are a bright star!','modal-theme1')">
    <div class="icon">🌟</div>
    <h1>Shine</h1>
    <p>Bright like a star</p>
  </div>
  <!-- more cards... -->
</div>

<div class="modal" id="modal">
  <div class="modal-content" id="modal-content">
    <canvas id="star-canvas"></canvas>
    <div class="stars" id="stars-container"></div>
    <h2 id="modal-title"></h2>
    <p id="modal-text"></p>
    <button class="close-btn" onclick="closeModal()">Close</button>
  </div>
</div>
```

#### CSS
```css
.card {
  /* Glassmorphism 스타일 */
}
.modal-content.modal-theme1 {
  background: linear-gradient(...);
}
.star {
  animation: twinkle 2s infinite, drift 20s infinite;
}
```

#### JavaScript
```js
function openModal(title, text, themeClass) {
  // 모달 오픈
}
function drawConstellation(themeClass) {
  // 캔버스에 선 그리기
}
```

---

## 🎨 커스터마이징 아이디어

- 별 개수, 크기, 움직임 속도 조절
- 모달에 추가 컨텐츠 (버튼, 링크 등)
- 별자리 패턴을 동적으로 생성

---

## 📝 라이선스

MIT © Kaltz

