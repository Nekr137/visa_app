function FromChoiceToInput(id_from,id_to){
    console.log('choice!')
    var s = $(id_from + ' option:selected').text()
    $(id_to).val(s);
}

$('#id_nationality_choice').on('click',function(){
    FromChoiceToInput('#id_nationality_choice','#id_nationality')
});
$('#id_placement_choice').on('click',function(){
    FromChoiceToInput('#id_placement_choice','#id_placement')
});
$('#id_rout_choice').on('click',function(){
    FromChoiceToInput('#id_rout_choice','#id_rout')
});
$('#id_organization_choice').on('click',function(){
    FromChoiceToInput('#id_organization_choice','#id_hostorganization')
});
$('#id_info_choice').on('click',function(){
    FromChoiceToInput('#id_info_choice','#id_additionalinfo')
});

$('.choice_action').on('click', function(){
    var s = $('.choice_action option:selected').text().split('/');
    $('#id_entry').val(s[0]);
    $('#id_departure').val(s[1]);
});

$('#id_ship_choice').on('click',function(){
    var ship_id = $('#id_ship_choice option:selected').val()
    console.log('id_ship_choice');
    console.log(csrf_token)
    $.ajax({
        url: '/rewrite_dates_in_form',
        type: 'post',
        data: {
                'ship_id' : ship_id,
                'csrfmiddlewaretoken': csrf_token,
            },
        success: function(resp)
        {
            console.log(resp)
            $("#date_choice_div_id")[0].innerHTML = resp;

            $('.choice_action').on('click', function(){
                var s = $('.choice_action option:selected').text().split('/');
                $('#id_entry').val(s[0]);
                $('#id_departure').val(s[1]);
            });
        },
    });
});