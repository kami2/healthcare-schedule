function datetime() {
    var currentTime = new Date()
    var Hour = currentTime.getHours() + 1
    var Minute = currentTime.getMinutes()
    var Second = currentTime.getSeconds()
    document.getElementById('zegarek').innerHTML(Hour+":"+Minute+":"+Second)
}