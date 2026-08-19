/**
* PHP Email Form Validation - v3.11
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');
      let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');
      
      if( ! action ) {
        displayError(thisForm, 'The form action property is not set!');
        return;
      }
      thisForm.querySelector('.loading').classList.add('d-block');
      let element = thisForm.querySelector('.error-message');
      if (element) {
        element.classList.remove('d-block');
      }
      let element2 = thisForm.querySelector('.sent-message');
      if (element2) {
        element2.classList.remove('d-block');
      }

      let formData = new FormData( thisForm );

      if ( recaptcha ) {
        if(typeof grecaptcha !== "undefined" ) {
          grecaptcha.ready(function() {
            try {
              grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
              .then(token => {
                formData.set('recaptcha-response', token);
                php_email_form_submit(thisForm, action, formData);
              })
            } catch(error) {
              displayError(thisForm, error);
            }
          });
        } else {
          displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
        }
      } else {
        php_email_form_submit(thisForm, action, formData);
      }
    });
  });

  async function php_email_form_submit(thisForm, action, formData) {
    try {
      const response = await fetch(action, {
        method: 'POST',
        body: formData,
        headers: {'X-Requested-With': 'XMLHttpRequest'}
      })

      const data = await response.json();
      if (!response.ok) {
              throw new Error(
                  data.message ||
                  'Form submission failed.'
              );
          }
          // Hide loading
      const loading =
          thisForm.querySelector('.loading');

      if (loading) {
          loading.classList.remove('d-block');
      }

      //display success
       const sentMessage =
            thisForm.querySelector('.sent-message');

      if (sentMessage) {

        sentMessage.innerHTML =
            data.message ||
            'Your message has been sent. Thank you!';

        sentMessage.classList.add('d-block');
      }
      thisForm.reset(); 

  }catch(error){
      const loading = thisForm.querySelector('.loading');
      if (loading) {
        loading.classList.remove("d-block");
      }
      displayError(thisForm, error);
    }
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    let element = thisForm.querySelector('.error-message');
    if (element) {
      element.innerHTML = error;
      element.classList.add('d-block');
    }
  }

})();
