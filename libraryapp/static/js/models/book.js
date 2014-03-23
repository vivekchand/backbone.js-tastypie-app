var app = app || {};

app.Book = Backbone.Model.extend({
    defaults: {
        title: 'No title',
        author: 'Unknown',
        release_date: 'Unknown',
    }
});

