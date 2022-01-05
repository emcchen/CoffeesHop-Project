'use strict';

function initMap() {
  console.log(document.querySelector('#map'))
  const map = new google.maps.Map(document.querySelector('#map'), {
    center: {
      lat: 37.773972,
      lng: -122.431297,
    },
    scrollwheel: false,
    zoom: 10,
    zoomControl: true,
    panControl: false,
  });

  document.querySelector('#geocode-address').addEventListener('click', () => {
    const userAddress = prompt('Enter location');

    const geocoder = new google.maps.Geocoder();
    geocoder.geocode({address: userAddress}, (results, status) => {
      if (status === 'OK') {
        const userLocation = results[0].geometry.location;

        new google.maps.Marker({
          position: userLocation,
          map,
        });

        map.setCenter(userLocation);
        map.setZoom(10);
      } else {
        alert(`Geocode was unsuccessful for the following reason: ${status}`);
      }
    });
  });

  // A single InfoWindow instance 
  const shopInfo = new google.maps.InfoWindow();
  const zipCode = document.querySelector('.zipcode').id

  // Retrieve shop info with AJAX
  fetch(`/map?zipcode=${zipCode}`)
  .then(response => response.json())
  .then(business_data => {
    for (const bis of business_data.businesses) {
      // Define the content of the infoWindow
      const shopInfoContent = `
      <div class="window-content">
        <div class="shop-thumbnail">
          <img
            src="/static/img/coffeeshop.jpg"
            alt="coffeeshop"
          />
        </div>

        <div class="map-shop-info">
          <b>${bis.name}</b> <br></br>
          <b>Address: </b>${bis.location.address1}, ${bis.location.zip_code}
        </div>
      </div>
    `;

      const shopMarker = new google.maps.Marker({
        position: {
          lat: bis.coordinates.latitude,
          lng: bis.coordinates.longitude,
        },
        // Shows shop ID when hovering over it 
        title: `Shop ID: ${bis.rating}`,
        icon: {
          url: '/static/img/tea-cup.svg',
          scaledSize: new google.maps.Size(50, 50),
        },
        map, // same as saying map: map
      });

      //Whatever window was open will close and new marker opens
      shopMarker.addListener('click', () => {
        shopInfo.close();
        shopInfo.setContent(shopInfoContent);
        shopInfo.open(map, shopMarker);
      });
    }
  })
}