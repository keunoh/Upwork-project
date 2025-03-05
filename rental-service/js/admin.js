function addVehicle() {
  let list = document.getElementById("vehicle-list");
  let li = document.createElement("li");
  li.innerText = "새로운 차량 추가됨";
  list.appendChild(li);
}

function initMap() {
  var map = new google.maps.Map(document.getElementById("map"), {
    center: {lat:37.5665, lng: 126.9780},
    zoom: 12
  });
}