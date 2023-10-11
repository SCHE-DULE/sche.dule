
const toastPlacementExample = document.querySelector('.toast-placement-ex');
let toastPlacement;

// Dispose toast when open another
function toastDispose(toast) {
  if (toast && toast._element !== null) {
    //if (toastPlacementExample) {
    //  toastPlacementExample.classList.remove(selectedType);
    //  DOMTokenList.prototype.remove.apply(toastPlacementExample.classList, selectedPlacement);
    //}
    toast.dispose();
  }
}

function showToast(title, message) {

  if (toastPlacement) {
    toastDispose(toastPlacement);
  }
  titleElement = document.querySelector('#toast_title');
  messageElement = document.querySelector('#toast_message');

  titleElement.textContent = title;
  messageElement.textContent = message;


  //toastPlacementExample.classList.add(selectedType);
  //DOMTokenList.prototype.add.apply(toastPlacementExample.classList, selectedPlacement);
  toastPlacement = new bootstrap.Toast(toastPlacementExample);
  toastPlacement.show();
};
