
function create_booking(id){
  $.ajax({url: "/home/createUserBooking/",
  data: {'row_id': id}
  });
}
