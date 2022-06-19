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


function toggleSuggestions(rowType, id, queryObject) {
	if($("#suggestions-row-"+rowType+String(id)).css("display") == "none") {
		$("#suggestions-row-"+rowType+String(id)).css("display", "table-row");
	} else {
		$("#suggestions-row-"+rowType+String(id)).css("display", "none");
	}
	var restUrl;
	if(rowType == "listing") {
		restUrl = "/rest/seekings/";
	} else if(rowType == "seeking") {
		restUrl = "/rest/listings/";
	} else {
		throw 'No rowType passed to toggleSuggestions!';
	}
	$.ajax({
		url : restUrl,
		type : 'GET',
		data : queryObject,
		dataType:'json',
		success : function(data) {
			html = '<td colspan=8>';
			n = data.length;
			n = n > 4 ? 4 : n;
			if(n == 0) {
				if(rowType == "listing") {
					html += '<h4>No matching Seekings found!</h4>';
					html += '<a href="/broker/listings/">See all Seekings</a>';
				}
				else if(rowType == "seeking") {
					html += '<h4>No matching Listings found!</h4>';
					html += '<a href="/broker/seekings/">See all Listings</a>';
				} else {
					throw 'No rowType passed to toggleSuggestions!';
				}
			} else {
				if(rowType == "listing") {
					html += '<table>';
					html += '<tr>';
					html += '<th>ID</th>';
					html += '<th>Type</th>';
					html += '<th>Start date</th>';
					html += '<th>Max price</th>';
					html += '<th>Tenant/Buyer name</th>';
					html += '<th>Number of persons</th>';
					html += '</tr>';
				} else if(rowType == "seeking") {
					html += '<table>';
					html += '<tr>';
					html += '<th>ID</th>';
					html += '<th>Type</th>';
					html += '<th>Available on</th>';
					html += '<th>Price</th>';
					html += '<th>Description</th>';
					html += '<th>Address</th>';
					html += '<th>Size</th>';
					html += '<th>Rooms</th>';
					html += '</tr>';
				} else {
					throw 'No rowType passed to toggleSuggestions!';
				}
			}
			if(rowType == "listing") {
				for(i = 0; i < n; i++) {
					html += '<tr>';
					html += '<td>'+data[i]['id']+'</td>';
					html += '<td>'+data[i]['seeking_type']+'</td>';
					html += '<td>' + getNiceDate(data[i]['starting_date']) + '</td>';
					if(data[i]['seeking_type'] == 'rental') {
						html += '<td>'+data[i]['max_rent']+'</td>';
					} else if(data[i]['seeking_type'] == 'for_sale') {
						html += '<td>'+data[i]['max_purchase_price']+'</td>';
					}
					html += '<td>' + data[i]['contact']['first_name'] + ' ' + 
						data[i]['contact']['last_name'] + '</td>';
					html += '<td>'+data[i]['number_of_persons']+'</td>';
					html += '</tr>';
				}
			} else if(rowType == "seeking") {
				for(i = 0; i < n; i++) {
					html += '<tr>';
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
			} else {
				throw 'No rowType passed to toggleSuggestions!';
			}
			if(n > 0) {
				html += '</table>';
			}
			html += '</td>';
			$("#suggestions-row-"+rowType+String(id)).html(html);
		},
		error : function(request,error) {
			alert("Request: "+JSON.stringify(request));
		}
	});
}
