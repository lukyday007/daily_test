<template>
  <h1>MAP</h1>
  <form @submit.prevent="searchPlaces">
    <select v-model="selectedCity" name="city" @change="updateDistricts">
      <option value=" 서울">서울특별시</option>
      <option value=" 부산">부산광역시</option>
      <option value=" 대구">대구광역시</option>
      <option value=" 인천">인천광역시</option>
      <option value=" 대전">대전광역시</option>
      <option value=" 울산">울산광역시</option>
      <option value=" 광주">광주광역시</option>
      <option value=" 세종">세종특별자치시</option>
      <option value=" 제주">제주특별자치도</option>
    </select>
    <select v-model="selectedDistrict" name="district">
      <option v-for="district in districts" :value="district">{{ district }}</option>
    </select>
    <select v-model="selectedBank" name="bank">
      <option value="신한은행">신한은행</option>
      <option value="하나은행">하나은행</option>
      <option value="국민은행" selected>국민은행</option>
      <option value="우리은행">우리은행</option>
      <option value="농협은행">농협은행</option>
    </select>
    <input type="submit" value="검색">
  </form>
  
  <KakaoMap :lat="37.566826" :lng="126.9786567" @onLoadKakaoMap="onLoadKakaoMap">
    <KakaoMapMarker
      v-for="(marker, index) in markerList"
      :key="marker.key === undefined ? index : marker.key"
      :lat="marker.lat"
      :lng="marker.lng"
      :infoWindow="marker.infoWindow"
      :clickable="true"
      @onClickKakaoMapMarker="onClickMapMarker(marker)"
    />
  </KakaoMap>
</template>

<script setup>
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps';
import { ref } from 'vue';

const map = ref();
const markerList = ref([]);
const selectedBank = ref("국민은행");
const selectedCity = ref(" 서울");
const selectedDistrict = ref("");
const districts = ref([]);

const cityDistricts = {
  " 서울": ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구", "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"],
  " 부산": ["중구", "서구", "동구", "영도구", "부산진구", "동래구", "남구", "북구", "해운대구", "사하구", "금정구", "강서구", "연제구", "수영구", "사상구", "기장군"],
  " 대구": ["중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군"],
  " 인천": ["중구", "동구", "미추홀구", "연수구", "남동구", "부평구", "계양구", "서구", "강화군", "옹진군"],
  " 대전": ["동구", "중구", "서구", "유성구", "대덕구"],
  " 울산": ["중구", "남구", "동구", "북구", "울주군"],
  " 광주": ["동구", "서구", "남구", "북구", "광산구"],
  " 세종": ["세종특별자치시"],
  " 제주": ["제주시", "서귀포시"]
};

const updateDistricts = () => {
  districts.value = cityDistricts[selectedCity.value];
  selectedDistrict.value = districts.value[0];
};

const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  searchPlaces(); // 페이지 로드 시 초기 검색 수행
};

const searchPlaces = () => {
  const bankname = selectedBank.value;
  const cityname = selectedCity.value.trim();
  const districtname = selectedDistrict.value.trim();
  console.log(bankname, cityname, districtname);
  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(`${bankname} ${cityname} ${districtname}`, placesSearchCB); // 공백 추가
};

const placesSearchCB = (data, status) => {
  markerList.value = [];
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();
    for (let marker of data) {
      const markerItem = {
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          content: marker.place_name,
          visible: false
        }
      };
      markerList.value.push(markerItem);
      bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
    }
    map.value?.setBounds(bounds);
  }
};

const onClickMapMarker = (markerItem) => {
  if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
    markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
  } else {
    markerItem.infoWindow.visible = true;
  }
};

// Initialize districts
updateDistricts();
</script>

<style scoped>
#map {
  width: 100%;
  height: 400px;
}
</style>
