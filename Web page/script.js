
function openGithubPage() {

    if (window.parent) {
        window.parent.location.href = "github.html";
    } else {
        window.location.href = "github.html";
    }
    return false;

}
function goHome(){
    if (window.parent) {
        window.parent.location.href = "home.html";
    } else {
        window.location.href = "home.html";
    }
    return false;
}