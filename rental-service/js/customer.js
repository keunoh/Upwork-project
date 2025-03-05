function processPayment() {
  let cardNumber = document.getElementById("card-number").value;
  if (cardNumber.length < 16) {
      alert("유효한 카드 번호를 입력하세요.");
  } else {
      alert("결제가 완료되었습니다!");
      window.location.href = "customer-confirm.html";
  }
}
