  let map;
      // Initialize and add the map
      function initMap() {
        // The location of Uluru
        const tlv = { lat: 32.09956781703534, lng: 34.774063172134504 };
        const beersheba= { lat: 31.23926535269584, lng: 34.7909099763604 };
        const mid= { lat: 31.61206658050883 , lng: 34.7905};
        // The map, centered at Uluru
        const map = new google.maps.Map(document.getElementById("map"), {
          zoom: 6.8,
          center: mid,
        });
        // The marker, positioned at Uluru
        const marker = new google.maps.Marker({
          position: tlv,
          map: map,
        });
        const marker1 = new google.maps.Marker({
          position: beersheba,
          map: map,
        });

      }
      window.initMap = initMap;
