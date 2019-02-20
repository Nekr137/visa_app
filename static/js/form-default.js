function FromChoiceToInput(id_from,id_to){
    var s = $(id_from + ' option:selected').text()
    $(id_to).val(s);
}

//Если с английского на русский, то передаём вторым параметром true.
transliterate = (
	function() {
		var
			rus = "щ   ш  ч  ц  ю  я  ё  ж  ъ  ы  э  а б в г д е з и й к л м н о п р с т у ф х ь".split(/ +/g),
			eng = "shh sh ch cz yu ya yo zh `` y' e` a b v g d e z i j k l m n o p r s t u f h `".split(/ +/g)
		;
		return function(text, engToRus) {
			var x;
			for(x = 0; x < rus.length; x++) {
				text = text.split(engToRus ? eng[x] : rus[x]).join(engToRus ? rus[x] : eng[x]);
				text = text.split(engToRus ? eng[x].toUpperCase() : rus[x].toUpperCase()).join(engToRus ? rus[x].toUpperCase() : eng[x].toUpperCase());
			}
			return text;
		}
	}
)();

// Изменение в имени
$('#id_firstname').on('change',function(){
    $('#id_familyname').val(transliterate($('#id_firstname').val(),true));
})
$('#id_lastname').on('change',function(){
    $('#id_name').val(transliterate($('#id_lastname').val(),true));
})

// Изменения в choice элементах
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
            //console.log(resp)
            $("#date_choice_div_id")[0].innerHTML = resp;

            $('.choice_action').on('click', function(){
                var s = $('.choice_action option:selected').text().split('/');
                $('#id_entry').val(s[0]);
                $('#id_departure').val(s[1]);
            });
        },
    });
});