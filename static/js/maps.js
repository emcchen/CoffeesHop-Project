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

    // A single InfoWindow instance 
    const shopInfo = new google.maps.InfoWindow();
    const zipCode = document.querySelector('.zipcode').id

    // Retrieve shop info with AJAX
    fetch(`/map?zipcode=${zipCode}`)
    .then(response => response.json())
    .then(business_data => {
      for (const bis of business_data['businesses']) {
        // Define the content of the infoWindow
        const shopInfoContent = `
        <div class="window-content">
          <div class="shop-thumbnail">
            <img
              src="/static/img/coffeeshop.jpg"
              alt="coffeeshop"
            />
          </div>

          <ul class="shop-info">
            <li><b>Term: </b>${bis['location']}</li>
            <li><b>Location: </b>${bis['coordinates']['latitude']}, ${bis['coordinates']['longitude']}</li>
          </ul>
        </div>
      `;

        const shopMarker = new google.maps.Marker({
          position: {
            lat: bis['coordinates']['latitude'],
            lng: bis['coordinates']['longitude'],
          },
         // Shows shop ID when hovering over it 
          title: `Shop ID: ${bis['rating']}`,
          icon: {
            url: '/static/img/polarBear.svg',
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