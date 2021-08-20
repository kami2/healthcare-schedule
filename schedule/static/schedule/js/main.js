var slider = {
	interval: 10,				//Czas między skokami bloku, w ms.
	pause: 3000,				//Czas pomiędzy dwoma kolejnymi blokami, w ms.
	stepLength: 10,				//Wartość skoku bloku, w px.
	showscount: 3,				//Ilosc przewiniec bloku po ktorym skoczy do reklamy
};

var obj = (function(){
	// some private stuff
	var hook = null;
	var elementHeight = 0;
	var stopped = false;
	var timer = null;
	var offset = 0;
	var lastIndex = 0;
	var index = 0;
	var counter = 0;

	var reset = function(){
	    offset = elementHeight;
            lastIndex = 0;
	    objs = 0;
            counter++;
            if(counter==slider.showscount) {
                window.document.location = reklama;
            }
	}

	var stop = function(){
		clearInterval(timer);
	}

	var start = function(){
		timer = setInterval(scroll, slider.interval);
	}

	var scroll = function(){
		offset -= slider.stepLength;

		index = Math.floor(offset/elementHeight);

		if(index!=lastIndex){
			lastIndex = index;
			stop();
			setTimeout(start, slider.pause);
		}

		hook.style.top = offset+'px';

		if(Math.abs(offset)>hook.clientHeight){
			reset();
		}

	}

	var init = function(){
		hook = document.getElementById('wrapper');
		elementHeight = hook.getElementsByTagName('div')[0].clientHeight+70;

		reset();
		start();
	}

	document.addEventListener('DOMContentLoaded', init, false);

	return {
		start: start,
		stop: stop,
		reset: reset
	}

})();

// obj.stop(); obj.start(); obj.reset();
