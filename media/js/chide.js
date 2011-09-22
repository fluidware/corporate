Router = Backbone.Router.extend({
	routes: {
		'!/': 'frontpage',
		'!/about/': 'about',
		'!/content/': 'content'
	},
	
	frontpage: function() {
		$('#content').load('/frontpage/');
	},
	
	about: function() {
		$('#content').load('/about/');
	},
	
	contact: function() {
		$('#content').load('/contact/');
	}
});

$(function() {
	var router = new Router;
	
	Backbone.history.start();
	
	if (!window.location.hash) {
		window.location.hash = '!/';
	}
});
