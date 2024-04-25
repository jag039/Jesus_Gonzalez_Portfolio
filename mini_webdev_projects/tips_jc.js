function calculateTotal() {
    var billAmount = document.getElementById("billNum").value;
    var tipP = document.getElementById("tip").value;
    

    var total = parseFloat(billAmount) + (parseFloat(billAmount)*(parseFloat(tipP)/100));
    total = total.toFixed(2)
    document.getElementById("result").innerText = "Total price: $" + total;
}