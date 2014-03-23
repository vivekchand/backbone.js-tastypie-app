var app = app || {};

app.Library = Backbone.Collection.extend({
    model: app.Book,
    url: '/api/v1/books/'
});
