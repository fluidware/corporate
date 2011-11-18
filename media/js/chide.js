Router = Backbone.Router.extend({
	routes: {
		'!/': 'frontpage',
		'!/about/': 'about',
		'!/contact/': 'contact'
	},
	
	load: function(url) {
		var div = $('<div><\/div>');
	
		div.load(url, function() {
			$('#content')
				.empty()
				.append(div);
		});
	},
	
	frontpage: function() {
		this.load('/frontpage/');
	},
	
	about: function() {
		this.load('/about/');
	},
	
	contact: function() {
		this.load('/contact/');
	}
});

$(function() {
	var router = new Router;
	
	Backbone.history.start();
	
	if (!window.location.hash) {
		window.location.hash = '!/';
	}
});
