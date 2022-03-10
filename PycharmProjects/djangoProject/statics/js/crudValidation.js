function validateFields() {
    clearErrorTexts();
    let userName;
	let firstName;
	let lastName;
	let email;

	if(document.getElementById("userName").value)
		userName = document.getElementById("userName").value;
	if(document.getElementById("firstName").value)
		firstName = document.getElementById("firstName").value;
	if(document.getElementById("lastName").value)
		lastName = document.getElementById("lastName").value;
    if(document.getElementById("emailId").value)
		email = document.getElementById("emailId").value;

    validateUserName(userName);
	validateFirstName(firstName);
	validateLastName(lastName);
	validateEmail(email);

    if((document.getElementById("userNameError").innerText.length==0 && document.getElementById("firstNameError").innerText.length==0 && document.getElementById("lastNameError").innerText.length==0 && document.getElementById("emailError").innerText.length==0))
		setTimeout(function(){ document.getElementById("form").submit(); }, 3000);


}

function validateUserName(userName)
{
	if(userName)
	{
	 if(!/^[a-zA-Z ]{2,30}$/.test(userName))
		 {
		 document.getElementById("userNameError").innerText="Key in a Valid User Name";
		 document.getElementById("userNameError").style.color="red";
		 }
	}
  else
	  {
	  document.getElementById("userNameError").innerText="User Name Field cannot be Empty";
	  document.getElementById("userNameError").style.color="red";
	  }

}

function validateFirstName(firstName)
{
	if(firstName)
	{
	 if(!/^[a-zA-Z ]{2,30}$/.test(firstName))
		 {
		 document.getElementById("firstNameError").innerText="Key in a Valid First Name";
		 document.getElementById("firstNameError").style.color="red";
		 }
	}
  else
	  {
	  document.getElementById("firstNameError").innerText="First Name Field cannot be Empty";
	  document.getElementById("firstNameError").style.color="red";
	  }

}

function validateLastName(lastName)
{
	if(lastName)
	{
	 if(!/^[a-zA-Z ]{2,30}$/.test(lastName))
		 {
		 document.getElementById("lastNameError").innerText="Key in a Valid User Name";
		 document.getElementById("lastNameError").style.color="red";
		 }
	}
  else
	  {
	  document.getElementById("lastNameError").innerText="Last Name Field cannot be Empty";
	  document.getElementById("lastNameError").style.color="red";
	  }

}

function validateEmail(email)
{
	if(email)
	{
	 if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)))
		 {
		 document.getElementById("emailError").innerText="Key in a Valid Email Id";
		 document.getElementById("emailError").style.color="red";
		 }
	}
  else
	  {
	  document.getElementById("emailError").innerText="Email Field cannot be Empty";
	  document.getElementById("emailError").style.color="red";
	  }

}

function deleteUser(userId) {
	let text = "Are you sure you want to delete the following user?";
	if(confirm(text))
        var xhr = new XMLHttpRequest();
        xhr.open('DELETE', '?deleteId='+userId, true);
	    xhr.send();
        location.reload();
}

function updateUser(userId,userName,firstName,lastName,email) {
        document.getElementById("userId").value = userId;
        document.getElementById("userName").value = userName;
        document.getElementById("firstName").value = firstName;
        document.getElementById("lastName").value = lastName;
        document.getElementById("emailId").value = email;
        document.getElementById("myForm").style.display = "block";
}

function clearErrorTexts() {
	document.getElementById("userNameError").innerText="";
	document.getElementById("firstNameError").innerText="";
	document.getElementById("lastNameError").innerText="";
	document.getElementById("emailError").innerText="";
}

function closeForm() {
	clearErrorTexts();
	document.getElementById("myForm").style.display = "none";
}
