function addgoods(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/addtogood/',
        type:'POST',
        dataType:'json',
        data:{'good_id':id},
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            if(data.code == '200'){
                $('.num_show').val(data.c_num)
                $('#countprice').html(data.price)
            }
        },
        error:function(data){
            alert('error')
        }
    })
}

function subgoods(id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url:'/app/subtogood/',
        type:'POST',
        dataType:'json',
        data:{'good_id':id},
        headers:{'X-CSRFToken': csrf},
        success:function(data){
            if(data.code == '200'){
                $('.num_show').val(data.c_num)
                $('#countprice').html(data.price)
            }
        },
        error:function(data){
            alert('error')
        }
    })
}

function get_re_detail() {
    var url = location.search
    var good_id = url.split('=')[1]
    $.get('/app/re_detail/?good_id='+good_id,function(data){
        if (data.code == '200'){
            $('.num_show').val(data.cart)
            $('#countprice').html(data.price)
        }
    })
}
get_re_detail()



function get_addtocart(id) {
    $.ajax({
        url:'/app/addtocart/',
        dataType:'json',
        type:'GET',
        data:{'good_id':id},
        success:function(data){
            if (data.code == '200') {
                alert('successful')
            }
        },
        error:function(data){
            alert('error')
        }
    })
}


