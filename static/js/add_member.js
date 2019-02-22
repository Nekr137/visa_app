// file for form2.html
// sends ajax post request to get a members_form

var m = document.getElementById('members');

//activates whet user press add_member btn
function add_m()
{
    console.log('add_member')
    NUM++;
    $.ajax({
        url: '/add_member',
        type: 'post',
        data: {'NUM':NUM,'csrfmiddlewaretoken': csrf_token},
        success: function(resp)
        {
            //console.log(resp)
            $("#members").append(resp);
            $('#NUM').val(NUM)
        },
    });
}

function delete_m(NUM)
{
    console.log('del')
    $("#member_id_"+NUM).remove()
    $('#NUM').val(NUM)
}