const socket = new WebSocket('ws://' + location.host + '/scan_websocket');
socket.addEventListener('message', ev => {
    log('<<< ' + ev.data, 'blue');
});