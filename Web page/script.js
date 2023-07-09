
function openGithubPage() {

    // Github doesn't allow embedding
    // if (window.parent) {
    //     window.parent.location.href = "github.html";
    // } else {
    //     window.location.href = "github.html";
    // }
    // return false;

    window.open('https://github.com/bryan6970/Data_sci_pw', '_blank');
}
function goHome(){
    if (window.parent) {
        window.parent.location.href = "home.html";
    } else {
        window.location.href = "home.html";
    }
    return false;
}