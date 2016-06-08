$(document).ready(function(){
	$("#btn1").click(function(){
		alert("Hello, yaphone");
	})
	$("#btn2").click(function(){
		var song = document.getElementById("input1").value;
		$.get("/search?song=" + song, function(data){
			alert(data);
		})
	})
})