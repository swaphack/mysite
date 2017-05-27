var mommodity;
if (mommodity != null) {
    alert("error define, namespace has existed!");
}

var mommodity = {

    autoMatchScreen: function() {
        var height = window.screen.height;
        var width = window.screen.width;

        $('.left').css("height", height);
        $('.right').css("height", height);
        
        $('.content').css("height", height);

        $('.middle').css("height",
            height - $('.header').height() - $('.footer').height());

    },
    autoSetEvent: function() {
        var search_value = $('#search_key').value;
        $('#search').attr("onclick", "search(" + search_value + ")");

        var item_urls = $('.item_url');
        item_urls.each(function(i) {
            var item_id = $(this).attr('itemId');
            $(this).attr("href", "javascript:showItemDetail(" + item_id + ")");
        });
    },

    init : function() {
    	var self = this;
    	self.autoMatchScreen();
    	self.autoSetEvent();
    }
}



window.onload = function() {
    mommodity.init();
}
