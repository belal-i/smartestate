function editInAdmin(modelType, modelId) {
	href = "/admin/";
	switch(modelType) {
		case "listing":
			href += "listings/listing/";
			break;
		case "seeking":
			href += "broker/seeking/";
			break;
		case "matching":
			href += "broker/matching/";
			break;
		default:
			break;
	}
	href += modelId + "/change/";
	window.location = href;
}
function prepareFormDataForRest(dataArray) {
	n = dataArray.length;
	returnObject = {};
	for(i = 0; i < n; i++) {
		field_name = dataArray[i].name;
		field_value = dataArray[i].value;
		switch(field_name) {
			default:
				if(field_value != "") {
					returnObject[field_name] = field_value;
				}
				break;

			/*
			TODO: See Feature #368.
			Rename some of these fields in the models, so that we can use
			use the same name for both seekings and listings??
			 * */
			case 'is_primary':
			case 'pets_ok':
			case 'has_pets':
			case 'has_internet':
			case 'must_have_internet':
			case 'is_furnished':
			case 'must_be_furnished':
			case 'is_smoker':
				returnObject[field_name] =
					field_value == "on" ? 'True' : 'False';
				break;
		}
	}
	return returnObject;
}
function getNiceDate(dateString) {
	dateObject = new Date(dateString);

	/*
	See Feature #303. Adjust date format based on language setting.
	 * */

	monthString = new Intl.DateTimeFormat('en-US', {month: 'long'}).format(dateObject);
	return monthString + ' ' + String(dateObject.getDate()) + ', ' + String(dateObject.getFullYear());
}
function getAge(dateString) {
	var today = new Date();
	var birthDate = new Date(dateString);
	var age = today.getFullYear() - birthDate.getFullYear();
	var m = today.getMonth() - birthDate.getMonth();
	if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
		age--;
	}
	return age;
}
function toggleRentalOrForSale() {
	model_type = $(".form-toggle-field:first").val();
	if(model_type == "rental") {
		$(".rental-form-fields").css({"display": "table-row"});
		$(".for-sale-form-fields").css({"display": "none"});
	} else if(model_type == "for_sale") {
		$(".rental-form-fields").css({"display": "none"});
		$(".for-sale-form-fields").css({"display": "table-row"});
	} else {
		$(".rental-form-fields").css({"display": "table-row"});
		$(".for-sale-form-fields").css({"display": "table-row"});
	}
}
$(".form-toggle-field").change(toggleRentalOrForSale);
$(".form-toggle-button").click(function() {
	$(".search-form").toggleClass("hidden-form");
});
function submitListingsSearch() {
	$.ajax({
		url : "/rest/listings/",
		type : 'GET',
		data : prepareFormDataForRest($("#listings-search").serializeArray()),
		dataType:'json',
		success : function(data) {
			html = "";
			n = data.length;
			for(i = 0; i < n; i++) {
				// See templates/broker/list-listing.html
				html += '<tr onclick="editInAdmin(\'listing\', '+data[i]['id']+');" class="broker-row">';
				html += '<td>'+data[i]['id']+'</td>';
				html += '<td>'+data[i]['listing_type']+'</td>';
				html += '<td>' + getNiceDate(data[i]['date_available']) + '</td>';
				if(data[i]['listing_type'] == 'rental') {
					html += '<td>'+data[i]['rental_price']+'</td>';
				} else if(data[i]['listing_type'] == 'for_sale') {
					html += '<td>'+data[i]['for_sale_price']+'</td>';
				}
				html += '<td>'+data[i]['short_description']+'</td>';
				html += '<td>' +
					data[i]['apartment']['house']['real_estate']['address']['street'] + ', ' +
					data[i]['apartment']['house']['real_estate']['address']['zip_code'] + ' ' +
					data[i]['apartment']['house']['real_estate']['address']['city'] +
					'</td>';
				html += '<td>'+data[i]['apartment']['size_sq_m']+'m<sup>2</sup></td>';
				html += '<td>'+data[i]['apartment']['number_of_rooms']+'</td>';
				html += '</tr>';
			}
			$("#listings-table-body").html(html);
		},
		error : function(request,error) {
			alert("Request: "+JSON.stringify(request));
		}
	});
}
$("#listings-search :input").change(submitListingsSearch);
$("#listings-search-submit").click(submitListingsSearch);
function submitSeekingsSearch() {
	$.ajax({
		url : "/rest/seekings/",
		type : 'GET',
		data : prepareFormDataForRest($("#seekings-search").serializeArray()),
		dataType:'json',
		success : function(data) {
			html = "";
			n = data.length;
			for(i = 0; i < n; i++) {
				// See templates/broker/list-seeking.html
				html += '<tr onclick="editInAdmin(\'seeking\', '+data[i]['id']+');" class="broker-row">';
				html += '<td>'+data[i]['id']+'</td>';
				html += '<td>'+data[i]['seeking_type']+'</td>';
				html += '<td>' + getNiceDate(data[i]['starting_date']) + '</td>';
				if(data[i]['seeking_type'] == 'rental') {
					html += '<td>'+data[i]['max_rent']+'</td>';
				} else if(data[i]['seeking_type'] == 'for_sale') {
					html += '<td>'+data[i]['max_purchase_price']+'</td>';
				}
				html += '<td>'+data[i]['min_number_of_rooms']+'</td>';
				html += '<td>' + data[i]['contact']['first_name'] + ' ' + 
					data[i]['contact']['last_name'] + '</td>';
				html += '<td>' + String(getAge(data[i]['contact']['date_of_birth'])) + '</td>';
				html += '<td>'+data[i]['number_of_persons']+'</td>';
				html += '<td>'+data[i]['occupation']+'</td>';
				html += '</tr>';
			}
			$("#seekings-table-body").html(html);
		},
		error : function(request,error) {
			alert("Request: "+JSON.stringify(request));
		}
	});
}
$("#seekings-search :input").change(submitSeekingsSearch);
$("#seekings-search-submit").click(submitSeekingsSearch);
function resetSearchForm() {
	$(".search-form:first").trigger("reset");
	toggleRentalOrForSale();
	try {
		submitListingsSearch();
	} catch {}
	try {
		submitSeekingsSearch();
	} catch {}
}
$(".form-reset-button").click(resetSearchForm);
function toggleSuggestions(rowType, id) {
	if($("#suggestions-row-"+rowType+String(id)).css("display") == "none") {
		$("#suggestions-row-"+rowType+String(id)).css("display", "table-row");
	} else {
		$("#suggestions-row-"+rowType+String(id)).css("display", "none");
	}
	/*
	TODO: Do the Ajax stuff here.
		*/
}
