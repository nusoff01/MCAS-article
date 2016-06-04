class DistrictsController < ApplicationController
	skip_before_action :verify_authenticity_token
	def new

	end

	def index
    	@districts = District.all
  	end

	def show
    	@district = District.find(params[:id])
  	end

	def create
		puts params
  		@district = District.new(district_params)
 
	  	@district.save
	  	redirect_to @district
	end

	def batchcreate
		# TBD: go through one district at a time and enter them in
	end
 
	private
	  	def district_params
	    	params.require(:district).permit(:name, :idnumber)
	  	end
end
