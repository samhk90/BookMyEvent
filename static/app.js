

const span = document.querySelector(".heart");
const i = document.getElementById("heart");

span.addEventListener("click", function(e) {
  i.classList.toggle("fa-heart");
  i.classList.toggle("fa-heart-o");
});

const bookingform =()=>{
  window.location.href="bookingform";
}
const event1=document.getElementById('event1');
event1.addEventListener("click",function(e){
  window.location.href="/book";
})
const price = document.getElementById('price');
const num_tickets = document.getElementById('numberOfTickets');
const cost = document.getElementById('cost');

