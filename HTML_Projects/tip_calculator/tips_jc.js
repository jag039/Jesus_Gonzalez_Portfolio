function calculateTotal() {
    var billAmount = document.getElementById("billNum").value;
    var tipP = document.getElementById("tip").value;

    if(billAmount == "" || tipP == "") {
        document.getElementById("result").innerText = "Please enter values before calculating";
    } else if(isNaN(parseFloat(billAmount)) || isNaN(parseFloat(tipP))) {
        document.getElementById("result").innerText = "Please enter numbers only";
    }
    else{
        var total = parseFloat(billAmount) + (parseFloat(billAmount)*(parseFloat(tipP)/100));
        total = total.toFixed(2)
        document.getElementById("result").innerText = "Total price: $" + total;        
    }
}