// show_block.js

// 페이지가 로드될 때 실행되는 함수
// 페이지가 로드될 때 실행되는 함수
window.onload = function () {
    // 각 버튼에 이벤트 리스너 추가
    const button1 = document.getElementById("show-button1");
    const button2 = document.getElementById("show-button2");
    const button3 = document.getElementById("show-button3");

    button1.addEventListener("click", function () {
        toggleInfo("Info1");
    });

    button2.addEventListener("click", function () {
        toggleInfo("Info2");
    });

    button3.addEventListener("click", function () {
        toggleInfo("Info3");
    });
};



// 정보를 토글하는 함수
function toggleInfo(infoId) {
    const infoDiv = document.getElementById(infoId);
    const isVisible = infoDiv.style.display === "none" ;

    infoDiv.classList.toggle("hidden-div-visible");
    //정보가 숨겨진 상태면 보이게, 보이는 상태면 숨김
    if (isVisible) {
        infoDiv.style.display = "none";
        return ;
    } else {
        infoDiv.style.display = "block";   
        return ;
    }
    
}
