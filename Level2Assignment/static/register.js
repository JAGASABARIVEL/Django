
    $(function(){
        function hideInputs() {
            if (document.getElementById('id_phone').value === document.getElementById('id_confirm_phone').value){
              alert("False")
            }
        }

        $("#id_confirm_phone").on('change', function(){
            hideInputs();
            }
        );

        hideInputs();
    });
