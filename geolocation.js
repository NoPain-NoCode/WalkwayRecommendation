const weather = document.querySelector(".js-weather");

const COORDS = 'coords';

const presentLatitude = 0;
const presentLongitude = 0;

function saveCoords(coordsObj) {
    localStorage.setItem(COORDS, JSON.stringify(coordsObj)); 
    //localstorage의 key, value 값은 모두 string 타입으로 저장되기때문에 변환시켜준다. 
    }

function handleSuccess(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const coordsObj = { // 객체의 key,  value 값이 동일할 때에는 한번만 써줘도 된다.
        latitude,       // localStorage에 객체로 value에 저장하기위해서 객체에 넣어준다.    
        longitude
    };
    saveCoords(coordsObj); // localStorage에 위치 저장 
}

function handleError() {
    console.log('cant not access to location');
}

function askForCoords() {
    console.log(navigator.geolocation.getCurrentPosition(handleSuccess, handleError));
}


function loadCoords() {
    const loadedCoords = localStorage.getItem(COORDS);
    if(loadedCoords === null) { 
        // localStorage에 좌표값이 저장되어있지않다면
        askForCoords(); // 좌표값을 물어본다
    }
    else{
        console.log(loadedCoords);
        
        const presentLatitude = parseFloat(loadedCoords.substring(12,22)) ;
        const presentLongitude   = parseFloat(loadedCoords.substring(35,46));

        console.log(typeof(presentLongitude));
        console.log(presentLatitude, presentLongitude);

        drawMap(presentLatitude,presentLongitude);
    } 
}

function drawMap(presentLatitude,presentLongitude){
    
        const myLatLng = {
            lat: presentLatitude,
            lng: presentLongitude
        }
        const map = new google.maps.Map(
            document.getElementById('recommend-map'),
            {
                //지도 초기화
                center: myLatLng,
                // 지도영역안에서 스크롤로 확대축소하는 것 막아줌.
                zoom: 12
            }
        )
        
        const marker = new google.maps.Marker({
            //현위치 표시해주는게 Marker. 정의해줌. 
            position: myLatLng,
            map: map,
            title: 'Location',
            icon: 'https://maps.google.com/mapfiles/ms/icons/red-dot.png'
        })
    
}

function init() {
    loadCoords();
}


const presentLocation = document.querySelector(".btn-recommend");
const showMap = document.querySelector(".show-map");

presentLocation.addEventListener('click', ()=>{
    showMap.classList.remove('hide');
    init();
})






