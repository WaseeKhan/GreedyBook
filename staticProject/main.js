$(document).ready(function(){
    console.log('World')
        $('#modal-btn').click(function(){
            console.log('Working')
            $('.ui.modal')
            .modal('show')
        ;
        })
        $('.ui.dropdown').dropdown()
})

