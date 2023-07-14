
function calculateNetSalary() {

    let salary = parseFloat(document.getElementById("basicSalary").value);


    let nightShift = document.getElementById("nightShift").checked;
    let nightShiftAllowance = 0;
    if (nightShift) {
        nightShiftAllowance = 500;
    }

    let pf = 0;
    let da = 0;
    let hra = 0;
    if (salary < 10000) {
        pf = 0.03 * basicSalary;
        da = 0.04 * basicSalary;
        hra = 0.025 * basicSalary;
    } else if (salary >= 10001 && salary <= 25000) {
        pf = 0.05 * salary;
        da = 0.06 * salary;
        hra = 0.045 * salary;
    } else if (salary > 25000) {
        pf = 0.07 * salary;
        da = 0.05 * salary;
        hra = 0.06 * salary;
    }


    let netSalary = salary + da + hra + nightShiftAllowance

    document.getElementById("result").value = netSalary;




}

