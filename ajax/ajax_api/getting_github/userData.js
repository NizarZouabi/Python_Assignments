
async function gitUserData() {
    var inputData = document.getElementById('api').value;
    var gitGet = "https://api.github.com/users/" + inputData;
    var showData = document.getElementById('user_data');
    var imgDisplay = document.getElementById('avatar');
    
    fetch(gitGet)
        .then(response => response.json())
        .then(function (response) {
            showData.innerHTML = response.login + ' ' + 'has' + ' ' + response.followers + ' ' + 'followers'
            imgDisplay.src = response.avatar_url
            console.log(response)
        })
        .catch(err => console.log(err))
}