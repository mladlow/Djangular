dogdateControllers = angular.module('dogdateApp.controllers', [])

dogdateControllers.controller('householdController', ($scope, $state, $log, households) ->
    $scope.households = households.all
)

dogdateControllers.controller('householdDetailController', ($scope, $state, $log, household) ->
    $scope.household = household
)
