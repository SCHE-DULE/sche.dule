$(document).ready(function () {
    $("#id_service").change(function () {
        var specialityId = $(this).val();
        $.ajax({
            url: "/accounts/get_therapists_by_speciality/",
            data: {'speciality_id': specialityId},
            dataType: 'json',
            success: function (data) {
                var therapistSelect = $("#id_therapist");
                therapistSelect.find('option:not(:first)').remove();
                $.each(data.therapists, function (index, therapist) {
                    therapistSelect.append($('<option>', {
                        value: therapist.id,
                        text: therapist.name
                    }));
                });
            }
        });
    });
});