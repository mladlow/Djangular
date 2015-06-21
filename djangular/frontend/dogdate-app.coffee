# module(<name>, [<deps>])
dogdateApp = angular.module('dogdateApp', ['ui.router', 'dogdateApp.controllers',
    #'dogdateApp.services', 'dogdateApp.directives'])
    'dogdateApp.services'])

# Just copying this for now - no idea where the providers come from :(
dogdateApp.config(($interpolateProvider, $stateProvider, $urlRouterProvider) ->
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
    # Default to household list
    $urlRouterProvider.otherwise('/')

    $stateProvider
        .state('householdlist'
            url: '/'
            templateUrl: 'householdList'
            controller: 'householdListController'
            resolve:
                households: (Households)->
                    Households.fetch()
                    return Households.data()
        )
        .state('householdDetail'
            url: '/{householdId:[0-9]+}/'
            templateUrl: 'householdDetail'
            controller: 'householdDetailController'
            resolve:
                household: ($stateParams, $log, Household)->
                    household = new Household(null)
                    household.get($stateParams.householdId)
                    return household
        )
)

dogdateApp.config(($httpProvider) ->
    getCookie = (name) ->
        for cookie in document.cookie.split ';' when cookie and name is (cookie.trim().split '=')[0]
            return decodeURIComponent cookie.trim()[(1 + name.length)...]
        null
    # Add Header to comply with Django's CSRF implementation
    $httpProvider.defaults.headers.common['X-CSRFToken'] = getCookie("csrftoken")
)
