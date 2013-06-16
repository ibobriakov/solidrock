/**
 * User: jackdevil
 */

MainApp.factory('aplInfoShare', function () {
    var personal_information = [],
        current_employment = [],
        previous_employments = [],
        educations = [],
        referees = [];

    return {
        personal_information: personal_information,
        current_employment: current_employment,
        previous_employments: previous_employments,
        educations: educations,
        referees: referees
    };
});

