function validate(){
    let mail=document.getElementById("mail").value;
    let pass=document.getElementById("mypassword").value;
    let exp=/^[a-zA-Z+0-9*]+@+[a-zA-Z]+\.[a-zA-Z]+/;

    if(mail=="" || !exp.test(mail))
    {
        alert("Enter valid email !");
    }

    else if(pass.length<5){
        alert("Password is too short !");
    }
    
}

function validate_signup(){

  let mail=document.getElementById("mail").value;
  let pass=document.getElementById("mypassword").value;
  let pass2=document.getElementById("mypassword2").value;
  let exp=/^[a-zA-Z+0-9*]+@+[a-zA-Z]+\.[a-zA-Z]+/;


  if(mail=="" || !exp.test(mail))
  {
      alert("Enter valid email !");
  }

  else if(pass.length<5){
      alert("Password is too short !");
  }

  else if(pass!=pass2){
    alert("Password not matched !");
  }
  

}

function myFunction() {
    var x = document.getElementById("mypassword");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }



