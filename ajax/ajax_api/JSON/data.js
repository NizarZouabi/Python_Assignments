var data = {
  "orders": [
    {
      "orderno": 784692,
      "date": "June 30, 2088 1:54:23 AM",
      "trackingno": "TN000391",
      "customer": {
        "custid": 11045,
        "fname": "Sue",
        "lname": "Hatfield",
        "address": "1409 Silver Street",
        "city": "Ashland",
        "state": "NE",
        "zip": 68003
      }
    },
    {
      "orderno": 784693,
      "date": "March 3, 2088 8:18:14 PM",
      "trackingno": "TN000468",
      "customer": {
        "custid": 11045,
        "fname": "Sue",
        "lname": "Hatfield",
        "address": "1409 Silver Street",
        "city": "Ashland",
        "state": "NE",
        "zip": 68003
      }
    }
  ]
}

console.log(typeof(data));
// 'object'
console.log(Array.isArray(data));
// false
console.log(Array.isArray(data.orders));
// true

// A - object
console.log(data);
// {orders: Array(1)}
// B - array at 'orders' key in object
console.log(data.orders);
// [{...}]
// C - object at index position 0 at 'orders' key in object
console.log(data.orders[0]);
// {"orderno": 784692, "date": "June 30, 2088 1:54:23 AM", "trackingno": "TN000391","customer": {...}}
// D - object at key 'customer' at index position 0 at 'orders' key in object
console.log(data.orders[0].customer);
// {"custid": 11045, "fname": "Sue", "lname": "Hatfield", "address": "1409 Silver Street", "city": "Ashland", ...}
// E - value at key 'address' in object at key 'customer' at index position 0 at 'orders' key in object
console.log(data.orders[0].customer.address);
// 1409 Silver Street