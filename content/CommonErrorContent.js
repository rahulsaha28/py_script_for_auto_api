/*
this is the base error middlewere
---------------------------------
{
  status: error code,
  errmess: message

}
---------------------------------
*/
// export base error middlewere
module.exports = (err, req, res, next) => {
  if (err?.message) {
    res.status(err?.status).json({
      status: err?.status,
      errmess: err?.message,
    });
  }
};
