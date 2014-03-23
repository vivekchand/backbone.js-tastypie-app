var app = app || {};

app.Book = Backbone.Model.extend({
    defaults: {
        title: 'No title',
        author: 'Unknown',
        releaseDate: 'Unknown',
    }
});
