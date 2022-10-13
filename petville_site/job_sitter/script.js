const progressBar = document.getElementById("progress-bar");
const progressNext = document.getElementById("progress-next");
const steps = document.querySelectorAll(".step");
let active = 1;
progressNext.addEventListener("click", () => {
	active++;
	if (active > steps.length) {
	  active = steps.length;
	}
	updateProgress();
  });
  const updateProgress = () => {
	// toggle active class on list items
	steps.forEach((step, i) => {
	  if (i < active) {
		step.classList.add("active");
	  } else {
		step.classList.remove("active");
	  }
	});
	// set progress bar width  
	progressBar.style.width = 
	  ((active - 1) / (steps.length - 1)) * 100 + "%";
	// enable disable prev and next buttons
	 if (active === steps.length) {
	  progressNext.disabled = true;
	} else {
	  progressNext.disabled = false;
	}
  };