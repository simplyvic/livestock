$(document).ready(function(){
     
    $(".dateinput").datepicker({changeYear: true,changeMonth: true});

    $('.tabs').tabs();
  	$('.pannel').accordion({active: false},{collapsible: true},{heightStyle: 'content'},{icons: {
                                                                                header: "ui-icon-plus",
                                                                                activeHeader: "ui-icon-minus"
                                                                              }
                                                                      }
                        );






 
});