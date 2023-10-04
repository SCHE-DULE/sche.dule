$(document).ready(function () {
    function getServicePkFromUrl() {
        var pathComponents = window.location.pathname.split('/');
        var index = pathComponents.indexOf('create');
        if (index !== -1 && index < pathComponents.length - 1) {
            return pathComponents[index + 1];
        }
        return null;
    }

    function updateTherapistsBySpeciality(specialityId) {
        $.ajax({
            url: "/accounts/get_therapists_by_speciality/",
            data: { 'speciality_id': specialityId },
            dataType: 'json',
            success: function (data) {
                var therapistSelect = $("#id_therapist");
                therapistSelect.find('option:not(:first)').remove();
                $.each(data.therapists, function (index, therapist) {
                    therapistSelect.append($('<option>', {
                        value: therapist.pk,
                        text: therapist.name
                    }));
                });
            }
        });
    }

    var servicePk = getServicePkFromUrl();
    console.log(servicePk);

    if (servicePk) {
        $('#id_service').val(servicePk);
        updateTherapistsBySpeciality(servicePk);
    }

    $("#id_service").change(function () {
        var specialityId = $(this).val();
        updateTherapistsBySpeciality(specialityId);
    });
});
