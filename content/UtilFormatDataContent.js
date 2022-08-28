/*
 return this form
 {
   success: true or false
   data: content data
   mess: any success message
 }
*/
// export formated data
module.exports = (data, mess = null) => {
  return {
    success: data ? true : false,
    data: data ? data : null,
    mess: data ? mess : null,
  };
};
