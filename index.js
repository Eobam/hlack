const c = document.getElementById("c");
const m = document.getElementById("m");
const ws = new WebSocket("ws://localhost:8080");
const view_channel_button = document.getElementById('viewchannelbutt');
const create_newchannel_butt = document.getElementById('createnewchannelbutt');
function rws(){
  let a = new WebSocket(`ws://localhost:${getnuminrange(9000, 65000)}`)
  return a
}
ws.onmessage = e => c.value += e.data + "\n";

function send() {
  const txt = m.value;
  ws.send(txt);
  c.value += "<You>: " + txt + "\n";
  m.value = "";
}

function getnuminrange(min, max) {
const minCeiled = Math.ceil(min);
const maxFloored = Math.floor(max);
return Math.floor(Math.random() * (maxFloored - minCeiled + 1)) + minCeiled; 
}


create_newchannel_butt.addEventListener('click', function() {
nchannelws = rws

} )