dogdateServices = angular.module('dogdateApp.services', [])

dogdateServices.factory('Household', ($http, $log) ->
    class Household
        constructor: (data) ->
            if data != null
                @init data

        init: (data) ->
            @address = data.address
            @city = data.city
            @state = data.state
            @zip_code = data.zip_code
            @fenced_yard = data.fenced_yard
        
        get: (householdId) ->
            $http({method: 'GET', url: '/dogdate/households/' + householdId + '/'})
                .success(data) =>
                    @init data
                    $log.info "Successfully fetched household"
                .error(data) =>
                    $log.info "Failed to fetch household"

    return Household
)

dogdateServices.factory('Households', ($log, $http, Household) ->
    households = {
        all : []
    }

    fromServer: (data) ->
        households['all'].length = 0
        for household in data
            households['all'].push(new Household(household))

    fetch: ->
        $http({method: 'GET', url: '/dogdate/households'})
            .success(data) =>
                @fromServer(data)
                $log.info "Successfully fetched households."
            .error(data) =>
                $log.info "Failed to fetch households."

    data: ->
        return households
)
