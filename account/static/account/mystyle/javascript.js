/* activate  and put color the white on the current url */
function my12() {  
				
		  for (var i = 0; i < document.links.length; i++) {
		  
			if (document.links[i].href == document.URL) {
				document.links[i].className = 'active';
				document.links[i].style.color = 'white';		
			} 
			else {
				document.links[0].className = 'active';
				document.links[0].style.color = 'white';
		}
	}
}	

// Get the modal
var modal1 = document.getElementById('id01');
function  f2(){
    modal1.style.display = 'none';
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
	}
}


/* activate  and put color the white on the current url */
function my(){  				
	var a = 0;
	var b = 0;		
	for (var i = 1; i < document.links.length; i++) { 
		if (document.links[i].href == document.URL) {
			a=1;
			b=i;
			i=document.links.length;
		}
	}			
	if (a==1){
		document.links[b].className = 'active';
		document.links[b].style.color = 'white';
	}
	else{
		document.links[1].className = 'active';
		document.links[1].style.color = 'white';
	}
}

