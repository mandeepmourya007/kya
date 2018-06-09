
// document.getElementById("f2").innerHTML=new Date();
var d2=60,d1=19,x,intervalid;

function decrement2()
{
d2--;
document.getElementById("f1").innerHTML=d1+":"+d2;
if(d2==0)
{
d2=60;
d1--;
}
if(x==1)
{
document.getElementById("start").disabled="disabled";
}
if(d1==-1&&d2==59)
 {
 alert("oops your time is over </br> submit now");
 }

}

function timeinterval()
{
x=1;
intervalid=setInterval(decrement2,1000);

}
function stoptest()
{
clearInterval(intervalid);
}

function tooglesidebar()
{
document.getElementById("sidebar").classList.toggle("active");
}
